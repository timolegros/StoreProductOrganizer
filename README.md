# StoreProductOrganizer #

**This is a very beginner project I did a few months ago for practice**

Simple script that analyzes 4 different files that contain products, suppliers, prices, and contact info. The program first utilizes the product ID's to find the lowest cost offered by any supplier for that product. Then the script calculates the amount that order should be by subtracting the number of available products from 50. Finally, the program matches the product ID's to the company offering that product and outputs a txt file containing all of this information in a hardcoded table.

- Onshelves.txt the first column contains product ID's and the second column contains the number of products onshelves.

- Products.txt the first column contains product ID's and the second column contains the product name.

- Suppliers.txt the first column contains supplier phone numbers and the second column contains the supplier name.

- Availability.txt contains product ID's in the first column, supplier phone numbers in the second column, and product prices in the last column.

- Orders.txt contains an example output that is printed to a txt file when the program is fed the four input files above.


**Known Issue: The last line printed in the output should print the second highest total order from a single supplier but currently prints the same supplier as the first.**
