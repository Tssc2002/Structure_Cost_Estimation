Structure Cost Estimation from 2D Plan (PDF/DWG)
This project provides a Python-based solution for estimating the cost of a construction project from 2D plans provided in PDF or DWG format. 
    The code extracts material quantities and calculates the total cost of construction, including detailed costs for concrete, steel, bricks, and sand based on predefined rates. 
    Additionally, it offers a stage-wise breakdown of costs for various construction phases like foundation, plinth, and superstructure.
Features
- PDF and DWG Parsing: Extracts relevant data from 2D architectural plans in PDF or DWG formats.
    - Material Quantities: Calculates quantities for materials such as concrete, steel, bricks, and sand.
    - Cost Calculation: Computes the total cost of materials based on predefined unit costs.
    - Stage-wise Breakdown: Provides a cost estimate for different construction stages (e.g., foundation, plinth, superstructure).
    - Output: Generates a detailed table showing material quantities, unit costs, and total costs, as well as the stage-wise cost breakdown.
Requirements
To run this project, ensure you have the following Python packages installed:
    - PyPDF2 (for parsing PDF files)
    - ezdxf (for reading DWG files)
    - pandas (for data manipulation and tabular output)
    - numpy (for numerical operations)
    You can install the required dependencies using the following command:
    ```bash
    pip install PyPDF2 ezdxf pandas numpy
    ```
    
Usage
1. Prepare Your Input Files
- The script supports input in PDF or DWG formats. Ensure that your file contains clear 2D architectural drawings with dimension details.
2. Run the Script
After installing the dependencies, use the script by providing the path to your PDF or DWG file as input:
    ```bash
    python estimate_cost.py path_to_your_file.pdf
    ```
    Or, if you have a DWG file:
    ```bash
    python estimate_cost.py path_to_your_file.dwg
    ```
    
3. Output
The script will output:
    1. Material Cost Table: A table with material types, quantities, unit costs, and total costs for each material.
    2. Stage-wise Construction Costs: A breakdown of costs for various construction stages, such as foundation, plinth, and superstructure.
Example Output
```text
    Material Cost Table:
        Material   Quantity   Unit  Unit Cost  Total Cost
    0  Concrete     200      m³      500       100000
    1    Steel       50      tons    70000     3500000
    2   Bricks     5000     units     10        50000
    3     Sand     300      m³      200        60000

    Stage-wise Construction Costs:
    Foundation: $600000.00
    Plinth: $300000.00
    Superstructure: $2100000.00
    ```
How It Works
1. Extracting Data
- PDF Files: The script uses PyPDF2 (or an alternative like pdfplumber) to extract text and dimensions from the PDF. 
    If OCR is needed for scanned plans, libraries like pytesseract can be added.
    - DWG Files: The script uses ezdxf to parse the DXF format of DWG files, extracting relevant entities such as lines, areas, and measurements.
2. Calculating Costs
- The script uses predefined unit costs for materials (concrete, steel, bricks, sand) to calculate the total cost based on quantities extracted from the 2D plan.
    - The cost is broken down into stages, with predefined percentages for different stages of construction (e.g., foundation: 20%, plinth: 10%, superstructure: 70%).
3. Displaying the Results
- The results are displayed in tabular format using the pandas library, making it easy to interpret and modify the calculations.
Customization
- Material Rates: The rates for materials like concrete, steel, bricks, and sand can be customized in the calculate_costs() function.
    - Construction Stages: You can modify the percentages for each construction stage (foundation, plinth, superstructure) based on the specific project requirements.
    - File Handling: For more robust file handling, additional checks for input file formats can be added.
Future Enhancements
- Enhanced PDF Parsing: Integration with OCR (using pytesseract) for scanned plans to read dimensions and text from images.
    - Advanced DWG Parsing: Implement parsing of more complex DWG file structures and layers to extract detailed information about different building elements.
    - Cost Breakdown by Labor: Include cost estimation for labor and machinery based on construction activities.
