def binaryPalin (self, N):
		# Your Code Here
		#number=int(input("Enter the Number"))
        binary_number=bin(N)[2:len(bin(N))]
        def check_palindrome(binary_number):
            if(binary_number==binary_number[::-1]):
                return True
            else:
                return False
        if(check_palindrome(binary_number)):
            return 1
        else:
            return 0
