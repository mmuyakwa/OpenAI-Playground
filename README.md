# OpenAI Playground

This is a repository for various AI-related scripts and experiments using the OpenAI API.

## Documentation

Detailed documentation for the code in this repository can be found in the respective markdown files within each directory.

## Requirements

The project dependencies are listed in the `requirements.txt` file. To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Automated Dependency Management

This repository uses Dependabot for automated dependency updates with the following configuration:

### Dependabot Configuration

- **Python dependencies**: Weekly updates every Monday at 09:00
- **GitHub Actions**: Weekly updates for workflow dependencies
- **Auto-merge**: Patch and minor updates are automatically merged after passing all checks
- **Manual review**: Major version updates require manual review

### Security Features

- Dependency review action scans for known vulnerabilities
- Security updates are grouped and prioritized
- All dependency changes are labeled appropriately

### Labels

- `dependencies`: All dependency updates
- `python`: Python package updates
- `github-actions`: GitHub Actions updates
- `automerge`: Automatically merged updates (patch/minor)
- `manual-review`: Updates requiring manual review (major)
- `patch`/`minor`/`major`: Update type indicators

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
