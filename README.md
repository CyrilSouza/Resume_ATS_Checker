# Resume_ATS_Checker

## Smart ATS

Smart ATS (Application Tracking System) is a tool designed to evaluate resumes based on given job descriptions. It utilizes Google's generative AI to match resumes with job descriptions and provide feedback on resume improvements.

## Installation

To run this project, you need to have Python installed. Clone the repository and install the dependencies using pip:

```
pip install -r requirements.txt
```

## Setup

Before running the application, you need to set up the GOOGLE_API_KEY environment variable with your Google API key.
```
$env:GOOGLE_API_KEY="your_api_key_here"
```

## Usage

Run the Streamlit application by executing the following command:
```
streamlit run app.py
```

1.In the Streamlit web interface, paste the job description in the text area provided.

2.Upload the resume in PDF format.

3.Click the "Submit" button to process the resume and view the ATS evaluation.


## Example

![WhatsApp Image 2024-02-11 at 22 05 16_32b47a8e](https://github.com/CyrilSouza/Resume_ATS_Checker/assets/95841357/7fe8dea3-3670-4029-82d9-983691112978)

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

