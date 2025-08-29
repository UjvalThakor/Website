from django.shortcuts import render

from django.shortcuts import render


def home(request):
    data = None
    if request.method == "POST":
        form_identifier = request.POST.get('form_identifier')  # Identify which form was submitted

        if form_identifier == "numeric_form":
            # Handle numeric form submission
            num1 = int(request.POST.get('firstno', 0))
            num2 = int(request.POST.get('secondno', 0))
            numeric_op = request.POST.get('operation1')

            # Perform numeric operations
            if numeric_op == "Add":
                data = num1 + num2
            elif numeric_op == "Sub":
                data = num1 - num2
            elif numeric_op == "Multi":
                data = num1 * num2
            elif numeric_op == "Divided":
                data = num1 / num2
            elif numeric_op == "Mod":
                data = num1 % num2
            elif numeric_op == "Floor Division":
                data = num1 // num2
            elif numeric_op == "Exponents":
                data = num1 ** num2
            else:
                print("Please check the numeric operation input")

        elif form_identifier == "string_form":
            # Handle string form submission
            name = request.POST.get('string-input', '')
            string_op = request.POST.get('Operation')

            # Perform string operations
            if string_op == "Uppercase":
                data = name.upper()
            elif string_op == "Lowercase":
                data = name.lower()
            elif string_op == "Capitalize":
                data = name.capitalize()
            elif string_op == "Join":
                data = name + " Jai Shree Ganesh"
            elif string_op == "Length":
                data = len(name)
            elif string_op == "Count":
                data = name.count('')
            else:
                print("Please check the string operation input")

    return render(request, 'templete.html', {'content': data})
