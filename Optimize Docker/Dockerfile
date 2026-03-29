# Stage 1: Build stage
FROM python:3.9-alpine as build-stage
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
COPY main.py .

# Stage 2: Run stage
FROM python:3.9-alpine
WORKDIR /app
COPY --from=build-stage /install /usr/local
COPY --from=build-stage /app/main.py .
COPY data.csv .
CMD ["python", "main.py"]

# The --no-cache-dir flag in the RUN pip install --no-cache-dir -r requirements.txt command is used to tell pip not to store
# the downloaded packages in its cache directory.
