# Copyright 2015, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import book_pb2
import book_pb2_grpc


def run():
	channel = grpc.insecure_channel('localhost:50051')
	stub = book_pb2_grpc.BookStub(channel)

	ans=True

	while ans:
		print ("""
			1.Add a Person
			2.Delete a Person
			3.List of Persons
			4.Exit/Quit
			""")
		ans=raw_input("What would you like to do? ") 
		if ans=="1":
			name = raw_input("Say a name: ")
			number = raw_input("Telephone")

			response = stub.AddPerson(book_pb2.Person(name=name, number=number))
			print("Book insert received: " + str(response.status))
			print("\n Person Added") 
			ans = True
		elif ans=="2":
			name = raw_input("Name: ")
			number = raw_input("Number")

			response = stub.RemovePerson(book_pb2.Person(name=name, number=number))
			if response.status:
				print("Done: " + str(response.status))				
				print("\n Person Removed") 
			ans = True
		elif ans=="3":
			response = stub.GetListOfPersons(book_pb2.Request(status=10))
			for x in response:
				print(x)
 
			ans = True
		elif ans=="4":
			print("\n Goodbye") 
		elif ans !="":
			print("\n Not Valid Choice Try again") 

if __name__ == '__main__':
	run()
