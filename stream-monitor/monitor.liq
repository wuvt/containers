set("log.file.path", "/dev/null")
set("log.stdout", true)

def blank_detected() =
    log("Stream silence detected")
    _ = get_process_lines("/data/silence.sh")
end

source = mksafe(input.https("https://stream.wuvt.vt.edu/wuvt.ogg"))

output.dummy(
    on_blank(max_blank=60.0, threshold=-40.0, track_sensitive=false, blank_detected, source))
