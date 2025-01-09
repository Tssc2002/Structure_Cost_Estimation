# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:30:27 2025

@author: srisa
"""
import PyPDF2
import ezdxf
import pandas as pd
import numpy as np
from collections import defaultdict

# Placeholder for function to extract material quantities from a PDF/DWG file
def extract_data_from_pdf(pdf_file):
    # Extract text and dimensions from PDF (e.g., using PyPDF2 or other libraries)
    extracted_data = {
        'areas': {'room_1': 100, 'room_2': 150},  # Example data
        'concrete_quantity': 200,  # Example in cubic meters
        'steel_quantity': 50,  # Example in tons
        'other_materials': {'bricks': 5000, 'sand': 300},  # Example in units
        'construction_stages': ['foundation', 'plinth', 'superstructure'],  # Example stages
    }
    return extracted_data

def extract_data_from_dwg(dwg_file):
    # Extract entities from DWG file (e.g., using ezdxf or other libraries)
    doc = ezdxf.readfile(dwg_file)
    extracted_data = {
        'areas': {'room_1': 120, 'room_2': 180},  # Example data
        'concrete_quantity': 250,  # Example in cubic meters
        'steel_quantity': 60,  # Example in tons
        'other_materials': {'bricks': 6000, 'sand': 350},  # Example in units
        'construction_stages': ['foundation', 'plinth', 'superstructure'],  # Example stages
    }
    return extracted_data

# Placeholder function to calculate costs based on extracted data
def calculate_costs(extracted_data):
    # Example material cost data (per unit)
    material_costs = {
        'concrete': 500,  # per cubic meter
        'steel': 70000,  # per ton
        'bricks': 10,  # per 1000 bricks
        'sand': 200,  # per cubic meter
    }
    
    # Placeholder cost calculation based on extracted data
    total_cost = 0
    cost_details = defaultdict(dict)
    
    for material, quantity in extracted_data['other_materials'].items():
        if material == 'bricks':
            cost_details['Bricks'] = quantity * material_costs['bricks'] / 1000
            total_cost += cost_details['Bricks']
    cost_details['Concrete'] = extracted_data['concrete_quantity'] * material_costs['concrete']
    total_cost += cost_details['Concrete']
    cost_details['Steel'] = extracted_data['steel_quantity'] * material_costs['steel']
    total_cost += cost_details['Steel']
    
    # Cost per construction stage (example breakdown)
    stage_costs = {
        'foundation': 0.2 * total_cost,
        'plinth': 0.1 * total_cost,
        'superstructure': 0.7 * total_cost,
    }

    # Convert the information into a DataFrame for easier visualization
    cost_table = pd.DataFrame({
        'Material': ['Concrete', 'Steel', 'Bricks', 'Sand'],
        'Quantity': [extracted_data['concrete_quantity'], extracted_data['steel_quantity'], 
                     extracted_data['other_materials']['bricks'], extracted_data['other_materials']['sand']],
        'Unit': ['m³', 'ton', 'units', 'm³'],
        'Unit Cost': [material_costs['concrete'], material_costs['steel'], 
                      material_costs['bricks'], material_costs['sand']],
        'Total Cost': [cost_details['Concrete'], cost_details['Steel'], 
                       cost_details['Bricks'], 0]  # sand cost calculation can be added here
    })
    
    return cost_table, stage_costs

# Main function to estimate the cost of the structure
def estimate_cost(file_path):
    # Check file extension to determine PDF or DWG
    if file_path.endswith('.pdf'):
        extracted_data = extract_data_from_pdf(file_path)
    elif file_path.endswith('.dwg'):
        extracted_data = extract_data_from_dwg(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a PDF or DWG file.")
    
    # Calculate costs
    cost_table, stage_costs = calculate_costs(extracted_data)
    
    # Display the cost table
    print("Material Cost Table:")
    print(cost_table)
    
    # Display stage-wise construction costs
    print("\nStage-wise Construction Costs:")
    for stage, cost in stage_costs.items():
        print(f"{stage}: ${cost:.2f}")
    
    # Return the cost table and stage costs
    return cost_table, stage_costs

# Example usage
file_path = 'example_structure.pdf'  # Provide the file path to a PDF or DWG file
estimate_cost(file_path)

