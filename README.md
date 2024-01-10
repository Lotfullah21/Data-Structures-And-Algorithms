### Documentation for Phani Daily Summary Form

### Overview

The Phani Daily Summary Form is a React component designed to collect and submit daily summary data related to various operations. The form is created using React, and it utilizes several external libraries such as Axios for making HTTP requests, React Toastify for displaying notifications, and Moment.js for handling date and time.

### Component Structure

The component is structured into sections, each handling a specific category of information. The form includes input fields, select dropdowns, and a submit button. The user can input data related to the daily summary, and upon submission, the data is sent to a Google Apps Script endpoint using Axios.

### State Management

The component uses React's useState hook to manage the state of various input fields. Each input field is associated with a specific piece of information, such as the number of POs in transit, DTDC delay calls, etc. The handleChange function is used to update the state when the user enters data into the corresponding input field.

### Form Submission

Upon form submission, the handleSubmit function is triggered. This function constructs a FormData object containing the entered data and sends a POST request to a Google Apps Script endpoint using Axios. The response is then checked, and a success or error notification is displayed using React Toastify. If the form submission is successful, the form fields are cleared.

### External Libraries

Axios: Used for making HTTP requests. In this case, it is utilized to send form data to a Google Apps Script endpoint.

### React Toastify: 
Used for displaying user-friendly notifications. Success and error messages are shown using Toastify's toast function.

### Moment.js: 
Used for handling date and time-related operations. Although it is imported, it is not currently used in the provided code. If there are plans to include date-related functionalities, Moment.js can be utilized.

### Form Fields
How Many PO Number In Transit?

Input for the number of POs currently in transit.
How many Po are in transit for more than 7 days?

Input for the number of POs in transit for more than 7 days.
How many Po are in transit for more than 15 days?

Input for the number of POs in transit for more than 15 days.
How many order placed but payment not received are there?

Input for the number of orders placed but payments not received.
How many payment successful but order not placed are there?

Input for the number of successful payments without corresponding orders.
Did you do BRS today?

Dropdown to select whether the user performed BRS (Bank Reconciliation Statement) on that day.
How many Po did you create?

Input for the number of Purchase Orders created.
Please share the PO numbers that you created today?

Input for providing a list of PO numbers created on that day.
How many DTDC Delay calls did you work on today?

Input for the number of DTDC delay calls worked on.
How many DTDC tickets did you raise today?

Input for the number of DTDC tickets raised.
How many DTDC tracking Id issues were solved today?

Input for the number of resolved DTDC tracking ID issues.
Please share the list of DTDC tracking IDs that were solved today?

Input for providing a list of solved DTDC tracking IDs.
How many Maruthi not delivered calls were made today?

Input for the number of calls made for Maruthi deliveries that were not successful.
How many Maruthi tickets were raised today?

Input for the number of Maruthi tickets raised.
How many Maruthi issues were solved today?

Input for the number of resolved Maruthi issues.
Please share the list of tracking IDs for Maruthi issues solved today?

Input for providing a list of tracking IDs for resolved Maruthi issues.
Submit Button

Button to submit the form.

### Usage
To use the SummaryForm component, include it in a parent React component or page. Users can fill out the form, and upon submission, the data will be sent to the specified Google Apps Script endpoint.

## jsx
Copy code
import React from "react";
import SummaryForm from "./SummaryForm";

const App = () => {
  return (
    <div>
      {/* Other components or content */}
      <SummaryForm />
    </div>
  );
};

export default App;


