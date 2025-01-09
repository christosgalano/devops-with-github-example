FROM python:3.10

# Create the fastapi user, which will be a non-root user
RUN adduser fastapi

WORKDIR /code

# Copy content
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Chown all the files to the fastapi user
RUN chown -R fastapi:fastapi $HOME

# Switch to the app user
USER fastapi

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
