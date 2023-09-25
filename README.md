# Google Cloud API Integration Guide

This guide provides step-by-step instructions to set up Google Cloud Speech-to-Text and Translation APIs in your Google Cloud Platform project.

## Step 1: Create a Project

1. Go to the [Google Cloud Platform Console](https://console.cloud.google.com/).
2. Click on the “Select a project” dropdown at the top right of the page.
3. Click on the “New Project” button to create a new project.
4. Enter a name for your project and click “Create”.

## Step 2: Enable APIs

1. Once the project is created, you will be taken to the Dashboard of your new project.
2. Click on the “Navigation Menu” (three horizontal lines) in the top left corner.
3. Go to “API & Services” → “Library”.
4. Search for “Cloud Speech-to-Text API” and click on it.
5. Click on the “Enable” button to enable this API for your project.
6. Go back to the API Library and search for “Cloud Translation API” and enable it in a similar way.

## Step 3: Create API Credentials

1. Once both APIs are enabled, go to “API & Services” → “Credentials” from the Navigation Menu.
2. Click on the “Create Credentials” button and select “Service account”.
3. Enter a name and description for the service account and click “Create”.
4. On the “Grant this service account access to project” page, you can assign a role to the service account. For testing purposes, you can use the “Project” → “Editor” role. For production use, assign only the necessary permissions following the principle of least privilege.
5. Click “Continue” and then “Done”.
6. Find the service account you just created in the list and click on it.
7. Under the “Keys” section, click “Add Key” and choose “JSON”.
8. A JSON key file will be downloaded to your computer. This file contains the credentials needed to access the APIs.

## Step 4: Set up API Credentials in Your Environment

1. Move the downloaded JSON key file to a secure location on your computer or server.
2. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the JSON key file. 
   ```sh
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"

