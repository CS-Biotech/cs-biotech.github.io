.PHONY: build serve clean

build:
	uv run pelican content

serve:
	uv run pelican --listen

clean:
	rm -rf output/
