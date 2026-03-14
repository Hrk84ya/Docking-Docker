package main

import (
	"fmt"
	"log"
	"net/http"
	"sync/atomic"
	"time"
)

var healthy atomic.Bool

func main() {
	// Simulate startup delay — app becomes healthy after 5 seconds
	healthy.Store(false)
	go func() {
		time.Sleep(5 * time.Second)
		healthy.Store(true)
		log.Println("App is now healthy")
	}()

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "Hello from the Healthcheck example!")
	})

	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		if healthy.Load() {
			w.WriteHeader(http.StatusOK)
			fmt.Fprintln(w, `{"status": "healthy"}`)
		} else {
			w.WriteHeader(http.StatusServiceUnavailable)
			fmt.Fprintln(w, `{"status": "starting"}`)
		}
	})

	log.Println("Server starting on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
