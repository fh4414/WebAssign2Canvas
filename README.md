# WebAssign2Canvas
This Python code manipulates WebAssign grade exports to match with the Canvas grade book export for merging.


1) Export and download the Canvas grades as a CSV file.
-- save this as "canvas.csv" (lowercase)
2) Export the grades from WebAssign
-- Go to "ScoreView"
-- Choose "All Assignments" 
-- Go to "Downloads"
-- Choose "comma-delimited values" as the file type
-- Click "Download"  
-- Change the file name to "webassign.csv"
3) Move both CSV files to the same folder as webassign_to_canvas.py (attached)
 -- Within webassign_to_canvas.py, change the variable "fold" to be this folder
4) Run webassign_to_canvas.py
-- This will create the file webassign_out.csv
-- Note any "Error with..." output from Python. Save these names for double checking later.
5) Open canvs.csv in Excel. 
-- Select cell B3, which should be the top student's ID number. Within "View," select "Freeze Panes" twice. 
-- Horizontally scroll unit you see the columns that correspond to the WebAssign grades to be imported.
6) From webassign_out.csv, select all (ctrl+a) and copy (ctrl+c).
7) Within canvas.csv, highlight a whole column near the columns to be modified and right-click. Insert copied cells. Shift right.
7) Scroll up and down canvas.csv to ensure the names all align. Note, the "Error with..." names were identified previously. You may need to highlight a row within the pasted section and delete via a right-click and "shift cells up".
8) Once alignment is confirmed between the pasted section and the original column A of canvas.csv, rearrange canvas.csv to mimic the original column organization. 
-- Delete the two columns with names pasted in.
-- Copy the valuable data in the pasted section and paste it under the column titles in the original canvas export.
-- Delete all rows that are no longer needed, including all of those that were created during the paste from webassign_out.csv.
9) Save the altered canvas.csv and import it into the Canvas grade book online.
