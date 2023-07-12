gcloud builds submit --tag gcr.io/my-project-388313/churn-prediction --project=my-project-388313

gcloud run deploy --image gcr.io/my-project-388313/churn-prediction --platform managed --project=my-project-388313 --allow-unauthenticated