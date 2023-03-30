# Programs commonly perform simulations of physical scenarios like cars in traffic, or people waiting at stores. A store wants to understand customer waiting time.
# A list provides the number of customers that arrive every minute for 10 minutes.
# The program should output the length of the line at each minute, assuming one clerk serves each customer and takes 1 minute to complete service.
# If the input is 2 0 0 2 1 0 0 0 1 0, the output should be 2 1 0 2 2 1 0 0 1 0 (At minute 0, 2 customers arrived in line.
# At minute 1, 1 of those has been served, reducing the line to 1. At minute 2, that customer was served, reducing the line to 0).
# Output a space after each output integer, including the last (followed by newline).
#
# HINTS:
#
# Every minute, if the lineLength wasn't 0, you can decrement lineLength because the clerk would have finished serving one customer.
#
# Every minute, if new customers arrived, just add them to lineLength for that minute.

def simulate_line(customer_arrivals):
    line_length = 0
    for num_customers in customer_arrivals: # for each customer arrival
        if line_length > 0: # you cant serve a customer if there are no customers to serve
            line_length -= 1  # Each minute, the clerk finishes serving 1 customer
        line_length += num_customers  # This many new customers arrived into line
        print(line_length, end=' ')
    print()


customer_arrivals = [int(input()) for _ in range(10)]
simulate_line(customer_arrivals)

