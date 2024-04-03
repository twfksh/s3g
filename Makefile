all: clean
	@mkdir public
	@python s3g.py

clean:
	@if exist public rmdir /s /q public
