.phony: clean
clean:
	rm -rf bin lib include local
	find . -name db.sqlite3 -print -delete
