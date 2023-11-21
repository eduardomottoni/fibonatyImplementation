# so, based on the introduction of algorithm of MIT, we will try to use the 
# temporary demonstration of the results during the process.


def apend_and_print(arr):
    print(arr)
    lastNumber = len(arr)-1
    sumedValue = arr[lastNumber]+arr[lastNumber-1]
    arr.append(sumedValue)
    if sumedValue % 2 == 0:
        evenNumberFibonacci.append(sumedValue)
    if sumedValue > 4000000:
        print(arr)
        return []
    return arr
    

firstnumber = 1
secondnumber = 1
Fibonacci = [firstnumber, secondnumber]
evenNumberFibonacci = []
print(type(Fibonacci))
print(len(Fibonacci))
# Fibonacci.append([firstnumber, secondnumber])

    
print(Fibonacci)

numberOfTerms = int(input("Please, type the number of terms you desire on Fibonacci sequence: "))
#loop
#print partial sequence

for i in range(numberOfTerms-1):
        Fibonacci = apend_and_print(Fibonacci)
        if Fibonacci == []:
            break
sum_even_numbers = sum(evenNumberFibonacci)
print(f'The even number list is {evenNumberFibonacci}')
print(f'the sum of all even terms of fibonnaci sequence is {sum_even_numbers:,}')