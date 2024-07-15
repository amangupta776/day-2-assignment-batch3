# Frappe Application Customization and Debugging

## Part 1: Custom Fields and Forms

### 1. Creating Custom Fields
- **Objective**: Add a custom field named Customer Anniversary (Date) to the Customer doctype.

### 2. Custom Form
- **Objective**: Customize the Customer form layout, add and make the Customer Anniversary field mandatory.

### 3. Validation Script
- **Objective**: Ensure Customer Anniversary date cannot be a future date.
- **Deliverables**:
  - Screenshots of the custom field creation.
  - Screenshot of the customized form.
  - Validation script.

## Part 2: Workflows

### 1. Designing a Workflow
- **Objective**: Create a workflow for the Sales Order doctype with states: Draft, Pending Approval, Approved, and Rejected.
- **Permissions**:
  - Draft to Pending Approval: Sales User
  - Pending Approval to Approved: Sales Manager
  - Pending Approval to Rejected: Sales Manager

### 2. Workflow Actions
- **Objective**: Add actions such as email notifications for state changes.
- **Deliverables**:
  - Workflow diagram.
  - Configuration details and screenshots.
  - Email notification script.

## Part 3: Print Formats

### 1. Creating a Custom Print Format
- **Objective**: Create a custom print format for Sales Invoice with company logo, custom header, item table layout, and custom footer.

### 2. Customizing the Print Format
- **Objective**: Include the Customer Anniversary field if available, using Jinja templating.
- **Deliverables**:
  - Custom print format code.
  - Screenshots of the printed Sales Invoice with the new format.

## Part 4: Scripts

### 1. Client Scripts
- **Objective**: Auto-calculate and update the Total Cost field in the Item doctype.

### 2. Server Scripts
- **Objective**: Send a notification email to the supplier when a Purchase Order is submitted.
- **Deliverables**:
  - Client script code.
  - Server script code.
  - Email notification template.

## Part 5: Permissions

### 1. Setting Up Role-Based Permissions
- **Objective**: Configure role-based permissions for the Project doctype.
  - **Roles**:
    - Project User: Can read and create projects.
    - Project Manager: Can read, create, and edit projects.
    - Project Admin: Full permissions, including delete.

### 2. Testing Permissions
- **Objective**: Test permissions with different roles.
- **Deliverables**:
  - Permission settings screenshots.
  - Results of permission testing.

## Section 1: Debugging Techniques

### 1. Using the Frappe Debugger
- **Objective**: Enable and use the Frappe debugger in your development environment.

### 2. Debugging Client Scripts
- **Objective**: Use browser developer tools to inspect elements, view console output, and set breakpoints.
- **Deliverables**:
  - Explanation and screenshots of using the Frappe debugger.
  - Screenshots or video demonstrating client script debugging.

## Section 2: Error Logs

### 1. Accessing Error Logs
- **Objective**: Access and resolve errors using Frappe error logs.

### 2. Custom Error Logging
- **Objective**: Log custom error messages and view them in the Frappe error log.
- **Deliverables**:
  - Steps to access error logs with screenshots.
  - Example of resolving a common error.
  - Custom error logging script and screenshots.

## Section 3: Console Output

### 1. Using Console Output for Debugging
- **Objective**: Use `console.log` in client scripts and `frappe.logger` in server scripts for debugging.

### 2. Analyzing Console Output
- **Objective**: Trace execution flow and identify issues using console output.
- **Deliverables**:
  - Script with console output statements.
  - Examples of console output for client and server scripts.
  - Explanation of issue resolution using console output.

## Section 4: Unit Testing

### 1. Writing Unit Tests
- **Objective**: Write unit tests for a custom function and use Frappe test runner to execute them.

### 2. Mocking Data for Tests
- **Objective**: Mock data for unit tests to cover various edge cases.
- **Deliverables**:
  - Unit test scripts.
  - Mock data examples and test results.
