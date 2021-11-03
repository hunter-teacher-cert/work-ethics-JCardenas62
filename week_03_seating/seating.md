# Plane Equity Proposal
The idea behind this proposal is to change the business strategies
of airlines. To do this, people who purchase multiple airline tickets
at once will have preferential seating choices. Those who purchase
more than 3 seats will be assigned rows.

1. To implement this, the first step would be to advertise the change in business model
to encourage people to buy airline tickets in groups.

2. Sanction about 1/4th of the seating capacity exclusively for solo
travelers. Sanction 1/4th of the seating capacity for either solo travelers or
groups known as the "reserve" seats. Sanction 1/2 of the seating capacity for group travelers.

3. Every time a purchase is made for one ticket, the person will
be assigned a random spot in the Solo travelers seats.

4. Every time a purchase is made for 3 tickets they will be given one row of
adjacent seats. This row will belong to the group travelers section.

5. Every time a purchase is made for 3 or more tickets, they will be given a row
of 3 seats, and the remaining seats will be assigned to row directly behind the first
assigned row. These seats will belong to the group travelers section.

6. If a purchase was made for 2 passengers, the program will first check in the
group travelers section for any incomplete rows. If the number of seats in the incomplete
row is equal to 2, then both passengers will be assigned those seats.
If there are no two adjacent empty seats in the group travelers section, then the
program will look for two adjacent empty seats in the Solo travelers section.
If there are no 2 adjacent empty seats, then they will be placed in the "reserve"
group.

7. If the solo travelers seating and the group travelers seating is full, the program
will assign them to the reserve seating.

8. If there is no more seating to accommodate pairs or groups, then the passengers will be assigned seats
randomly.

9. If one ticket is purchased and there is no more space in either the solo travelers group
or the reserve group, the program will look within the group travelers section
for any incomplete rows and assign them a seat there.

10. If the plane is near capacity and cannot accommodate
groups or pairs, in any of the 3 sections, then a message will display no more available seats.

11. If the plane is at capacity and cannot accommodate any single seat, then a message
will display that no more seats are available.
