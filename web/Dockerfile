FROM python:3.9.2

# Set Python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Python packages
ADD requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Run the image as a non-root user
ARG uid=1000
ARG gid=1000
RUN groupadd --gid ${gid} django \
    && useradd --uid ${uid} --gid ${gid} django
USER django