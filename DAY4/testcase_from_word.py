import docx
import pandas as pd

# Step 1: Read the Word file using python-docx
file_path = 'C:\\Users\\Admin\\Desktop\\DA_\\TestCase.docx'  # Replace with your actual file path
doc = docx.Document(file_path)

# Step 2: Identify the "Test Scenarios" section and extract the content
test_scenarios_start = None
test_case_details = []
current_scenario = {}

# Iterate over each paragraph to identify the "Test Scenarios" section
for para in doc.paragraphs:
    # Check if this is the beginning of the "Test Scenarios" section
    if 'Test Scenarios' in para.text:
        test_scenarios_start = True
        continue  # Skip this line (it just marks the section start)
    
    # After finding the start of the "Test Scenarios", we begin extracting test case details
    if test_scenarios_start:
        if para.text.strip() == '':  # Empty line indicates the end of a test case
            if current_scenario:  # Save the previous scenario details
                test_case_details.append(current_scenario)
                current_scenario = {}  # Reset for the next test case
        else:
            # Extracting details for each scenario
            # Assuming the test case ID and description are in the same line or paragraph
            if 'Test Case ID' in para.text:
                current_scenario['Test Case ID'] = para.text.strip()
            elif 'Description' in para.text:
                current_scenario['Test Case Description'] = para.text.strip()
            elif 'Expected Result' in para.text:
                current_scenario['Expected Result'] = para.text.strip()
            # Add more fields as necessary (steps, conditions, etc.)
        
# Add the last test case if the document ends without an empty line
if current_scenario:
    test_case_details.append(current_scenario)

# Step 3: Compile the extracted test case details into a DataFrame
df = pd.DataFrame(test_case_details)

# Step 4: Write the DataFrame to an Excel file (.xls)
output_file = 'extracted_test_cases.xlsx'
df.to_excel(output_file, index=False)

print(f"Test cases have been successfully extracted and saved to {output_file}")
