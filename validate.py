#!/usr/bin/env python3
"""
Simple validation script for the Cursor Admin API OpenAPI specification.
This script performs basic YAML syntax validation and structural checks.
"""

import yaml
import json
import sys
from pathlib import Path

def validate_yaml_syntax(file_path):
    """Validate YAML syntax."""
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        print("✅ YAML syntax is valid")
        return True
    except yaml.YAMLError as e:
        print(f"❌ YAML syntax error: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return False

def validate_openapi_structure(file_path):
    """Validate basic OpenAPI structure."""
    try:
        with open(file_path, 'r') as file:
            spec = yaml.safe_load(file)
        
        # Check required top-level fields
        required_fields = ['openapi', 'info', 'paths']
        missing_fields = []
        
        for field in required_fields:
            if field not in spec:
                missing_fields.append(field)
        
        if missing_fields:
            print(f"❌ Missing required fields: {', '.join(missing_fields)}")
            return False
        
        # Check OpenAPI version
        if not spec['openapi'].startswith('3.'):
            print(f"❌ Unsupported OpenAPI version: {spec['openapi']}")
            return False
        
        # Check info section
        info = spec['info']
        if 'title' not in info or 'version' not in info:
            print("❌ Missing required info fields (title, version)")
            return False
        
        # Check paths
        if not spec['paths']:
            print("❌ No paths defined")
            return False
        
        print("✅ Basic OpenAPI structure is valid")
        return True
        
    except Exception as e:
        print(f"❌ Structure validation error: {e}")
        return False

def validate_endpoints(file_path):
    """Validate endpoint definitions."""
    try:
        with open(file_path, 'r') as file:
            spec = yaml.safe_load(file)
        
        paths = spec.get('paths', {})
        endpoint_count = 0
        
        for path, methods in paths.items():
            for method, operation in methods.items():
                if method in ['get', 'post', 'put', 'delete', 'patch']:
                    endpoint_count += 1
                    
                    # Check required operation fields
                    if 'summary' not in operation:
                        print(f"⚠️  Missing summary for {method.upper()} {path}")
                    
                    if 'responses' not in operation:
                        print(f"❌ Missing responses for {method.upper()} {path}")
                        return False
        
        print(f"✅ Found {endpoint_count} valid endpoints")
        return True
        
    except Exception as e:
        print(f"❌ Endpoint validation error: {e}")
        return False

def validate_components(file_path):
    """Validate components section."""
    try:
        with open(file_path, 'r') as file:
            spec = yaml.safe_load(file)
        
        components = spec.get('components', {})
        
        # Count schemas
        schemas = components.get('schemas', {})
        print(f"✅ Found {len(schemas)} schema definitions")
        
        # Count security schemes
        security_schemes = components.get('securitySchemes', {})
        print(f"✅ Found {len(security_schemes)} security scheme definitions")
        
        # Count responses
        responses = components.get('responses', {})
        print(f"✅ Found {len(responses)} reusable response definitions")
        
        return True
        
    except Exception as e:
        print(f"❌ Components validation error: {e}")
        return False

def generate_summary(file_path):
    """Generate a summary of the API specification."""
    try:
        with open(file_path, 'r') as file:
            spec = yaml.safe_load(file)
        
        print("\n📊 API Specification Summary")
        print("=" * 40)
        
        # Basic info
        info = spec.get('info', {})
        print(f"Title: {info.get('title', 'N/A')}")
        print(f"Version: {info.get('version', 'N/A')}")
        print(f"Description: {info.get('description', 'N/A')[:100]}...")
        
        # Servers
        servers = spec.get('servers', [])
        print(f"Servers: {len(servers)}")
        for server in servers:
            print(f"  - {server.get('url', 'N/A')} ({server.get('description', 'N/A')})")
        
        # Paths summary
        paths = spec.get('paths', {})
        methods_count = {}
        
        for path, methods in paths.items():
            for method in methods.keys():
                if method in ['get', 'post', 'put', 'delete', 'patch']:
                    methods_count[method.upper()] = methods_count.get(method.upper(), 0) + 1
        
        print(f"Total Paths: {len(paths)}")
        print("HTTP Methods:")
        for method, count in sorted(methods_count.items()):
            print(f"  - {method}: {count}")
        
        # Components summary
        components = spec.get('components', {})
        schemas = components.get('schemas', {})
        print(f"Schema Definitions: {len(schemas)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Summary generation error: {e}")
        return False

def main():
    """Main validation function."""
    file_path = Path(__file__).parent / 'cursor-admin-api-openapi.yaml'
    
    print("🔍 Validating Cursor Admin API OpenAPI Specification")
    print("=" * 60)
    
    # Run all validations
    validations = [
        validate_yaml_syntax(file_path),
        validate_openapi_structure(file_path),
        validate_endpoints(file_path),
        validate_components(file_path),
    ]
    
    # Generate summary
    generate_summary(file_path)
    
    # Final result
    print("\n" + "=" * 60)
    if all(validations):
        print("🎉 All validations passed! The OpenAPI specification is valid.")
        sys.exit(0)
    else:
        print("❌ Some validations failed. Please check the errors above.")
        sys.exit(1)

if __name__ == '__main__':
    main()