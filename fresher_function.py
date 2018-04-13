

def print_hello():
	print "hello"

print_hello()


def print_str(s):
  print s *2
  return s *2

print_str("yes")

def print_default(s="hello"):
  print s
print_default()
print_default("default")

def print_args(s,*argu):
	print s
	for a in argu:
		print a
	return

print_args("hellp")
print_args("hello", "world", "77")

print_str("..................................")
def print_two(a, b):
	print a, b

print_two("a", "b")



print_str("...............................")


def print_argus(s,*argu):
	print s
	for a in argu:
		print a
	return

print_argus("help")
print_argus("hello", "world", "88")