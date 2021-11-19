Nov 19 2021

Hello,
Here is the Python file I have created to merge WebAssign grades with Canvas. It's not foolproof, but it's helpful. To run this, you'll need a basic understanding of both Python and Excel. Let me know if you have any questions or recommendations.
Best,
Chris


1) Export and download the Canvas grades as a CSV file.
-- save this as "canvas.csv" (lowercase)
2) Export the grades from WebAssign
-- Go to "ScoreView"
-- Choose "All Assignments" 
-- Go to "Downloads"
-- Choose "comma-delimited values" as the file type
-- Click "Download"  
-- Change the file name to "webassign.csv"
3) Move both CSV files to the same folder as webassign_to_canvas.py (attached) 
-- Within webassign_to_canvas.py, change the variable "fold" to be this folder
4) Run webassign_to_canvas.py
-- This will create the file webassign_out.csv
-- Note any "Error with..." output from Python. Save these names for double-checking later.
5) Open canvas.csv in Excel. 
-- Select cell B3, which should be the top student's ID number. Within "View," select "Freeze Panes" twice. 
-- Horizontally scroll to see the columns that correspond to the WebAssign grades to be imported, assuming that these columns were previously created in Canvas and you are just entering numbers.
6) From webassign_out.csv, select all (ctrl+a) and copy (ctrl+c).
7) Within canvas.csv, highlight a whole column near the columns to be modified and right-click. Insert copied cells. Shift right.
8) Scroll up and down canvas.csv to ensure the names all align. Compare the first column in canvas.csv and the first columns from webassign_out.csv. Note, the "Error with..." names were identified previously. You may need to highlight a row within the pasted section and delete via a right-click and "shift cells up".
9) Once alignment is confirmed between the pasted section and the original column A of canvas.csv, rearrange canvas.csv to mimic the original column organization. 
-- Delete the columns with student names from webassign_out.csv.
-- Copy the valuable data in the pasted section and paste it under the column titles in the original canvas export, assuming these columns were already present. Alternatively, you can create new columns in canvas.csv that will require confirmation during the Canvas grade import.
10) Save the altered canvas.csv and import it into the Canvas grade book online.
-- Note the new columns you are creating and the grades you are changing.


---
Christopher V. Kelly
Associate Professor
Department of Physics and Astronomy
Wayne State University
666 W. Hancock St.Detroit, MI 48201
Email: cvkelly@wayne.edu
Web: https://cvkelly.wayne.edu
Pronouns: he/him
