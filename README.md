# PHAIT - Personal Health AI Tracker

A secure, AI-powered medical vault that operates entirely on-device to provide emergency medical information access, longitudinal health insights, and preventive health monitoring.

## Features

- **Complete Data Sovereignty**: All health records stored locally with AES-256-GCM encryption
- **Emergency SOS Access**: Instant access to critical medical information for first responders
- **AI-Powered Insights**: Local AI models analyze health trends without cloud transmission
- **Offline-First**: Full functionality without internet connectivity
- **Multi-Language Support**: Emergency summaries in English, Spanish, French, German, and Mandarin
- **Comprehensive Tracking**: Medications, vital signs, lab results, and medical documents

## Installation

```bash
pip install -e .
```

For development:
```bash
pip install -e ".[dev]"
```

## Quick Start

```bash
# Initialize PHAIT
phait init

# Add a health record
phait add-record --type prescription --title "Medication X" --content "Take daily"

# View emergency SOS summary
phait emergency-access

# Create backup
phait backup --output ~/phait-backup.enc
```

## Project Structure

- `phait/storage/` - Encrypted database and data persistence
- `phait/security/` - Authentication and encryption services
- `phait/application/` - Business logic for health tracking
- `phait/ai/` - Local AI model integration
- `phait/ui/` - User interface components
- `tests/` - Unit, property-based, and integration tests

## Security

PHAIT prioritizes your privacy:
- All data encrypted at rest with AES-256-GCM
- No cloud synchronization or external data transmission
- Configurable emergency access modes
- Secure deletion of sensitive data

## Testing

```bash
# Run all tests
pytest

# Run property-based tests only
pytest tests/property/

# Run with coverage
pytest --cov=phait
```

## License

MIT
