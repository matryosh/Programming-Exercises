principal = float(input("What is the principal amount? "))
roi = float(input("What is the rate? "))
years= float(input("What is the number of years? "))
times_compounded = float(input("What is the number of times the interest\nis compound per year? "))

compound_interest = principal * ((1+((roi/ 100)/times_compounded))**(times_compounded*years))

print("${} invested at {}% for {} years\ncompounded {} times per year is ${:.2f}".format(int(principal),
                                                                                      roi,
                                                                                      int(years),
                                                                                      int(times_compounded),
                                                                                      compound_interest))
