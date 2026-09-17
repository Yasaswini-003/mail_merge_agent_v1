from pathlib import Path
import pandas as pd
import zipfile


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Default files
TEMPLATE_FILE = BASE_DIR / "certificate.docx"
EXCEL_FILE = BASE_DIR / "Student_Data.xlsx"
OUTPUT_DIR = BASE_DIR / "output"


# Required Excel columns
REQUIRED_COLUMNS = [
    "Student Name",
    "Roll No",
    "Coordinator",
    "HOD",
]


def validate_excel_file(excel_path: str = str(EXCEL_FILE)) -> str:
    """
    Validate the Excel file:
    1. Check that the file exists.
    2. Check that the required columns exist.
    3. Check that the Excel file contains records.
    4. Check that all required fields are filled.
    """

    path = Path(excel_path)

    # Check Excel file
    if not path.exists():
        return f"Excel file not found: {path}"

    # Read Excel
    try:
        df = pd.read_excel(path)
    except Exception as e:
        return f"Could not read Excel file: {e}"

    # Check required columns
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        return (
            "Validation failed. Missing columns: "
            + ", ".join(missing_columns)
        )

    # Check empty Excel
    if df.empty:
        return (
            "Validation failed. "
            "The Excel file contains no student records."
        )

    # Check missing values in required fields
    missing_values = []

    for index, row in df.iterrows():

        student_name = str(row["Student Name"]).strip()
        roll_no = str(row["Roll No"]).strip()
        coordinator = str(row["Coordinator"]).strip()
        hod = str(row["HOD"]).strip()

        missing_fields = []

        if pd.isna(row["Student Name"]) or not student_name or student_name == "nan":
            missing_fields.append("Student Name")

        if pd.isna(row["Roll No"]) or not roll_no or roll_no == "nan":
            missing_fields.append("Roll No")

        if pd.isna(row["Coordinator"]) or not coordinator or coordinator == "nan":
            missing_fields.append("Coordinator")

        if pd.isna(row["HOD"]) or not hod or hod == "nan":
            missing_fields.append("HOD")

        if missing_fields:

            display_name = (
                student_name
                if student_name and student_name != "nan"
                else f"Row {index + 2}"
            )

            display_roll = (
                roll_no
                if roll_no and roll_no != "nan"
                else "No Roll No"
            )

            missing_values.append(
                f"{display_name} ({display_roll}) -> "
                + ", ".join(missing_fields)
            )

    # Stop if any required value is missing
    if missing_values:
        return (
            "Validation failed. The following required fields are missing:\n"
            + "\n".join(missing_values)
            + "\n\nNo certificates should be generated."
        )

    return (
        f"Validation successful. "
        f"Found {len(df)} student records. "
        f"All required fields are filled."
    )


def replace_in_docx_xml(input_file, output_file, replacements):
    """
    Replace placeholders throughout the DOCX XML.

    Handles text in:
    - normal paragraphs
    - tables
    - text boxes
    - shapes
    - headers
    - footers
    - other Word XML content
    """

    with zipfile.ZipFile(input_file, "r") as zin:
        with zipfile.ZipFile(
            output_file,
            "w",
            zipfile.ZIP_DEFLATED
        ) as zout:

            for item in zin.infolist():

                data = zin.read(item.filename)

                # Process Word XML files
                if item.filename.endswith(".xml"):

                    try:
                        text = data.decode("utf-8")

                        for old_text, new_text in replacements.items():
                            text = text.replace(old_text, new_text)

                        data = text.encode("utf-8")

                    except UnicodeDecodeError:
                        pass

                zout.writestr(item, data)


def generate_certificates(excel_path: str = str(EXCEL_FILE)) -> str:
    """
    Generate one personalized certificate for every student.

    The Excel file is validated before any certificate is generated.
    If any required field is missing, generation stops completely.
    """

    excel_path = Path(excel_path)

    # Check template
    if not TEMPLATE_FILE.exists():
        return f"Certificate template not found: {TEMPLATE_FILE}"

    # Check Excel file
    if not excel_path.exists():
        return f"Excel file not found: {excel_path}"

    # Read Excel
    try:
        df = pd.read_excel(excel_path)
    except Exception as e:
        return f"Could not read Excel file: {e}"

    # Validate required columns
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        return (
            "Cannot generate certificates. Missing columns: "
            + ", ".join(missing_columns)
        )

    # Check empty Excel
    if df.empty:
        return "No student records found."

    # IMPORTANT:
    # Validate every required value before generating ANY certificate.
    validation_result = validate_excel_file(str(excel_path))

    if not validation_result.startswith("Validation successful"):
        return (
            "Certificate generation stopped.\n\n"
            + validation_result
        )

    # Create output folder
    OUTPUT_DIR.mkdir(exist_ok=True)

    generated_files = []

    # Process every student
    for _, row in df.iterrows():

        student_name = str(row["Student Name"]).strip()
        roll_no = str(row["Roll No"]).strip()
        coordinator = str(row["Coordinator"]).strip()
        hod = str(row["HOD"]).strip()

        # Placeholder replacements
        replacements = {
            "{{STUDENT_NAME}}": student_name,
            "{{ROLL_NO}}": roll_no,
            "{{COORDINATOR}}": coordinator,
            "{{HOD}}": hod,
        }

        # Create safe filename
        safe_name = "".join(
            character
            if character.isalnum() or character in " _-"
            else "_"
            for character in student_name
        ).strip()

        output_file = (
            OUTPUT_DIR
            / f"{safe_name}_{roll_no}.docx"
        )

        # Copy certificate and replace placeholders
        replace_in_docx_xml(
            TEMPLATE_FILE,
            output_file,
            replacements
        )

        generated_files.append(str(output_file))

    # Final result
    if not generated_files:
        return "No certificates were generated."

    return (
        f"Successfully generated "
        f"{len(generated_files)} certificates:\n"
        + "\n".join(generated_files)
    )