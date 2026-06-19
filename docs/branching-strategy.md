# Branching Strategy

## Branch Types
- **main**: Production-ready code
- **develop**: Integration branch for features
- **feature/***: New features (e.g., feature/data-ingestion)
- **hotfix/***: Critical bug fixes (e.g., hotfix/security-patch)
- **release/***: Release preparation (e.g., release/v1.0.0)

## Naming Conventions
- Features: feature/SC-123-description
- Hotfixes: hotfix/v1.0.1-description
- Releases: release/v1.0.0

## Workflow
1. Create from develop: git checkout -b feature/description
2. Work on feature
3. Commit frequently with descriptive messages
4. Push to remote
5. Create PR to develop
6. After approval, squash and merge
