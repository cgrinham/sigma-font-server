# Sigma Font Server
Quick and dirty server for loading fonts into figma.
Not in any way affiliated with figma, the Rust implementation was broken
and it was quicker to write this than learn how to write Rust to fix it :)

# How to run
This is not meant to be a permanent solution so just install the dependencies then
run the flask debug server on port 18412:
`FONT_DIR=/home/myname/.myfontdir flask run app -p 18412`
