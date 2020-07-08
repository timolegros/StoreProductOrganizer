# StoreProductOrganizer
Simple script that analyzes 5 different files that contain products, suppliers, prices, and contact info to output the best supplier for each product.

Onshelves.txt the first column contains product ID's and the second column contains the number of products onshelves.

Products.txt the first column contains product ID's and the second column contains the product name.

Suppliers.txt the first column contains supplier ID's and the second column contains the supplier name.

Availability.txt contains product ID's in the first column, supplier ID's in the second column, and product prices in the last column.

Orders.txt contains an example output that is printed to a txt file when the program is fed the four input files above.


**Known Issue: The last line printed in the output should print the second highest total order from a single supplier but currently prints the same supplier as the first. 
