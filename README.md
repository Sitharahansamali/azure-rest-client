# Azure REST Client - Language Detection

A Python REST client application that uses Azure AI Services (Text Analytics) to detect the language of text input.

## Features

- 🌐 Language detection using Azure Cognitive Services Text Analytics API
- 🔐 Secure API key management with environment variables
- 📊 Returns detected language with confidence score
- 🚀 Simple command-line interface

## Prerequisites

- Python 3.11 or higher
- Azure AI Services account with Text Analytics API enabled
- Valid Azure AI Services endpoint and API key

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd rest-client
```

2. Install dependencies using uv:
```bash
uv sync
```

Or install manually:
```bash
uv pip install requests python-dotenv
```

## Configuration

1. Create a `.env` file in the `src/` directory:
```bash
touch src/.env
```

2. Add your Azure AI Services credentials to the `.env` file:
```env
AI_SERVICE_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/
AI_SERVICE_KEY=your-api-key-here
```

> **Important:** Never commit your `.env` file to version control. Make sure it's listed in your `.gitignore`.

## Usage

Run the language detection client:

```bash
python src/rest_client.py
```

You'll be prompted to enter text:
```
Enter text to analyze: Bonjour, comment allez-vous?
```

Sample output:
```
Document Id: 1
Detected Language: French
Confidence Score: 0.99
```

## Project Structure

```
rest-client/
├── src/
│   ├── rest_client.py    # Main REST client for language detection
│   └── .env              # Environment variables (not in repo)
├── main.py               # Application entry point
├── pyproject.toml        # Project configuration and dependencies
└── README.md             # This file
```

## Dependencies

- **requests** (>=2.32.5) - HTTP library for making API calls
- **python-dotenv** (>=0.9.9) - Environment variable management

## API Reference

### `detect_language(text)`

Detects the language of the provided text using Azure Text Analytics API.

**Parameters:**
- `text` (str): The text to analyze

**Returns:**
- Prints document ID, detected language name, and confidence score

**API Endpoint:**
- `/text/analytics/v3.1/languages`

## Error Handling

The application includes basic error handling:
- Prints HTTP status codes and error messages if the API call fails
- Validates response status before processing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is for educational purposes as part of Azure certification training.

## Additional Notes

- This project uses Azure Cognitive Services Text Analytics API v3.1
- Ensure your Azure subscription has sufficient credits/quota
- The API supports detecting over 120 languages

## Troubleshooting

**Issue: "Error: 401"**
- Check that your `AI_SERVICE_KEY` is correct in the `.env` file

**Issue: "Error: 404"**
- Verify your `AI_SERVICE_ENDPOINT` URL is correct
- Ensure the endpoint includes the protocol (https://)

**Issue: Module not found**
- Run `uv sync` or `uv pip install requests python-dotenv`

---

For more information about Azure Text Analytics API, visit the [official documentation](https://learn.microsoft.com/azure/cognitive-services/language-service/).
