![ss](./N8N/screenshot.png)

# Dropshipping Workflow Documentation

This document describes the structure and logic of the `dropshipping` n8n workflow, which automates order processing, tracking, and notifications for a dropshipping business.

---

## Overview

The workflow manages:
- New order creation and notification
- Order tracking and status updates
- Order cancellation and refund notifications
- Communication with customers and suppliers via email
- Integration with Airtable for data storage and retrieval

---

## Main Components

### 1. **Triggers**
- **Webhook**: Entry point for API requests (e.g., new order, tracking, cancellation).

### 2. **Order Processing**
- **Switch**: Routes incoming requests based on `operationType` (`new_order`, `track`, `cancel`, `ror`).
- **adding_order**: Upserts new order data into Airtable (`dropshiiping orders` table).
- **user_details**: Fetches user details from Airtable.
- **product_details**: Fetches product details from Airtable.
- **AI Agent**: Summarizes order details for customer emails using OpenAI.
- **customer-mailing**: Sends summarized order details to the customer.
- **Airtable2**: Fetches supplier details.
- **supplier_mail**: Notifies the supplier of a new order.

### 3. **Order Tracking**
- **Switch1**: Routes tracking requests based on `source` (`customer` or `seller`).
- **fetching_parcel_location**: Retrieves parcel location from Airtable.
- **send_tracking_details**: Emails tracking info to the customer.
- **updating_parcel_location**: Updates parcel status in Airtable.
- **send_tracking_details_on_update**: Notifies customer of updated parcel status.
- **tracking_deatail_ondemand**: Sends tracking updates on demand.

### 4. **Order Cancellation & Refund**
- **cancel_update**: Updates order status to "Cancelled" in Airtable.
- **user_deatails**: Fetches user details for cancellation notification.
- **Gmail**: Notifies customer of cancellation.
- **return_and_refund_manager**: Notifies manager of cancellation/refund.
- **STATUS_FETCH**: Upserts order status as "Pending" (used for status management).

### 5. **AI & Utility Nodes**
- **OpenAI Chat Model**: Provides language model for AI Agent.
- **Sticky Notes**: Visual documentation within the workflow.
- **Code**: (Sample) Adds a field to all items (for demonstration).
- **Text Classifier**: (Disabled) For classifying incoming emails.
- **Hugging Face Inference Model**: (Disabled) For advanced AI inference.

---

## Data Flow

1. **New Order**
    - Webhook → Switch (`new_order`) → adding_order → product_details & user_details
    - user_details → AI Agent → customer-mailing
    - product_details → Airtable2 → supplier_mail

2. **Tracking**
    - Webhook → Switch (`track`) → Switch1
    - Switch1 (`customer`) → fetching_parcel_location → send_tracking_details
    - Switch1 (`seller`) → updating_parcel_location → send_tracking_details_on_update & Airtable1 → tracking_deatail_ondemand

3. **Cancellation**
    - Webhook → Switch (`cancel`) → cancel_update → user_deatails → Gmail
    - cancel_update → STATUS_FETCH → return_and_refund_manager

---

## Airtable Tables Used

- **dropshiiping orders**: Stores order details.
- **user**: Stores user/customer details.
- **products**: Stores product information.
- **tracking**: Stores parcel tracking information.
- **supplier_details**: Stores supplier contact info.

---

## Email Notifications

- **customer-mailing**: Order summary to customer.
- **supplier_mail**: New order details to supplier.
- **send_tracking_details / send_tracking_details_on_update / tracking_deatail_ondemand**: Tracking updates to customer.
- **Gmail**: Order cancellation to customer.
- **return_and_refund_manager**: Cancellation/refund alert to manager.

---

## AI Integration

- **AI Agent**: Uses OpenAI to summarize order details for customer emails.

---

## Visual Aids

- **Sticky Notes**: Used throughout the workflow for section labeling and documentation.

---

**End of Documentation**
