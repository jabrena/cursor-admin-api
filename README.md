# Cursor Teams Admin API - OpenAPI Specification

This repository contains the OpenAPI 3.0 specification for the Cursor Teams Admin API, developed based on the official [Cursor Teams Admin API documentation](https://cursor.com/docs/account/teams/admin-api) and inspired by the structure of the [Background Agents OpenAPI specification](https://cursor.com/docs-static/background-agents-openapi.yaml).

## 📋 Overview

The Cursor Teams Admin API provides comprehensive functionality for managing teams, users, and organizational settings within the Cursor platform. This API enables administrators to:

- **Team Management**: Create, update, delete, and list teams
- **Member Management**: Add, remove, and manage team member roles
- **User Management**: Create, update, and manage user accounts
- **Organization Settings**: Configure organization-wide policies and settings

## 🗂️ API Structure

### Base URL
- **Production**: `https://api.cursor.com/v1`
- **Staging**: `https://staging-api.cursor.com/v1`

### Authentication
The API uses Bearer token authentication with JWT tokens:
```
Authorization: Bearer <your-jwt-token>
```

### Main Endpoints

#### Teams (`/teams`)
- `GET /teams` - List all teams (with pagination and search)
- `POST /teams` - Create a new team
- `GET /teams/{teamId}` - Get team details
- `PUT /teams/{teamId}` - Update team information
- `DELETE /teams/{teamId}` - Delete a team

#### Team Members (`/teams/{teamId}/members`)
- `GET /teams/{teamId}/members` - List team members
- `POST /teams/{teamId}/members` - Add a member to the team
- `GET /teams/{teamId}/members/{userId}` - Get member details
- `PUT /teams/{teamId}/members/{userId}` - Update member role
- `DELETE /teams/{teamId}/members/{userId}` - Remove member from team

#### Users (`/users`)
- `GET /users` - List all users (with pagination and filtering)
- `POST /users` - Create a new user account
- `GET /users/{userId}` - Get user details
- `PUT /users/{userId}` - Update user information
- `DELETE /users/{userId}` - Delete user account

#### Organization Settings (`/organizations/settings`)
- `GET /organizations/settings` - Get organization settings
- `PUT /organizations/settings` - Update organization settings

## 📊 Key Features

### Comprehensive Schema Definitions
- **Team**: Complete team information with member counts and timestamps
- **User**: User profiles with status tracking and team memberships
- **TeamMember**: Member-specific information including roles and join dates
- **OrganizationSettings**: Configurable organization policies

### Advanced Functionality
- **Pagination**: All list endpoints support limit/offset pagination
- **Search & Filtering**: Search teams and users by name, email, or other criteria
- **Role Management**: Granular role control (admin, member, viewer)
- **Status Tracking**: User and team status management (active, inactive, pending)

### Robust Error Handling
- Standardized error responses with detailed messages
- Proper HTTP status codes for different scenarios
- Validation error details for form submissions
- Request ID tracking for debugging

## 🔧 Usage Examples

### Create a New Team
```bash
curl -X POST https://api.cursor.com/v1/teams \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Data Science Team",
    "description": "Team focused on data science and machine learning"
  }'
```

### Add a Member to a Team
```bash
curl -X POST https://api.cursor.com/v1/teams/team_123/members \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user_456",
    "role": "member"
  }'
```

### List Teams with Search
```bash
curl -X GET "https://api.cursor.com/v1/teams?search=engineering&limit=10" \
  -H "Authorization: Bearer <token>"
```

## 📝 Data Models

### Team Object
```json
{
  "id": "team_123",
  "name": "Engineering Team",
  "description": "Main engineering team",
  "member_count": 15,
  "created_at": "2023-01-15T10:30:00Z",
  "updated_at": "2023-06-20T14:45:00Z",
  "status": "active"
}
```

### User Object
```json
{
  "id": "user_456",
  "email": "john.doe@example.com",
  "name": "John Doe",
  "avatar_url": "https://example.com/avatars/user_456.jpg",
  "status": "active",
  "created_at": "2023-01-10T09:15:00Z",
  "updated_at": "2023-06-15T11:30:00Z"
}
```

### Team Member Object
```json
{
  "user_id": "user_789",
  "email": "member@example.com",
  "name": "Alice Johnson",
  "avatar_url": "https://example.com/avatars/user_789.jpg",
  "role": "member",
  "joined_at": "2023-03-01T12:00:00Z",
  "status": "active"
}
```

## 🚀 Getting Started

### 1. Validate the Specification
```bash
# Using swagger-codegen
swagger-codegen validate -i cursor-admin-api-openapi.yaml

# Using openapi-generator
openapi-generator validate -i cursor-admin-api-openapi.yaml
```

### 2. Generate Documentation
```bash
# Generate HTML documentation
swagger-codegen generate -i cursor-admin-api-openapi.yaml -l html2 -o docs/

# Or use Redoc
redoc-cli build cursor-admin-api-openapi.yaml
```

### 3. Generate Client SDKs
```bash
# Generate JavaScript client
openapi-generator generate -i cursor-admin-api-openapi.yaml -g javascript -o clients/javascript/

# Generate Python client
openapi-generator generate -i cursor-admin-api-openapi.yaml -g python -o clients/python/

# Generate Go client
openapi-generator generate -i cursor-admin-api-openapi.yaml -g go -o clients/go/
```

## 🔒 Security Considerations

- **Authentication**: All endpoints require valid JWT tokens
- **Authorization**: Role-based access control for different operations
- **Rate Limiting**: API includes standard rate limiting (implementation dependent)
- **Input Validation**: Comprehensive input validation with detailed error messages
- **HTTPS Only**: All API communication must use HTTPS

## 📚 Additional Resources

- [OpenAPI 3.0 Specification](https://swagger.io/specification/)
- [Cursor Documentation](https://cursor.com/docs)
- [JWT Authentication Guide](https://jwt.io/introduction)
- [REST API Best Practices](https://restfulapi.net/)

## 🤝 Contributing

When contributing to this OpenAPI specification:

1. Ensure all new endpoints follow the established patterns
2. Include comprehensive examples for request/response bodies
3. Add appropriate error handling for all scenarios
4. Update this README with any new functionality
5. Validate the specification before submitting changes

## 📄 License

This OpenAPI specification is provided as documentation for the Cursor Teams Admin API. Please refer to Cursor's terms of service for usage guidelines.

---

**Note**: This specification is based on publicly available documentation and common API patterns. For the most up-to-date and official API documentation, please refer to the [official Cursor documentation](https://cursor.com/docs/account/teams/admin-api).