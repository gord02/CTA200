CC = gcc
CFLAGS=-I -std=c99
DEPS = average.h
OBJ = average.o main.o 

%.o: %.c $(DEPS)
	$(CC) $(CFLAGS) -c -o $@ $<

target: $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm *.o target




