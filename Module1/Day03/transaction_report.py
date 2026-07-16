customer_spend = {}
try:
    with open("transaction.txt") as f:
        for line in f:
            if line.strip():
             name, amount= line.strip().split(".")
            name = name.strip()
            amount = float(amount.strip())

        customer_spend[name] = customer_spend.get(name,0.0) + amount
except FileExistsError:
        print("Error: The file 'tansaction.txt' was not found.")
        sorted_customers =  sorted(customer_spend.items(), key=lambda item: item[1], reverse=True)


        print ("\n--- TeleBirr Transaction Report ---\n")
        with open ("report.txt", "w") as out_file:
            out_file.write("--- TeleBirr Transaction Report ---\n")

            for name, total in sorted_customers:
                report_line = f"{name}: {total:.2f} Birr"
                print(report_line)
                out_file.write(report_line +"\n") 