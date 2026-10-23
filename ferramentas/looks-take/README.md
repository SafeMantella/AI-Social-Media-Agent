# Take looks and transition sound

Contract only. Filter graphs from one copy named a brand's grade. Rebuild them from `memory/visual_identity_standard.md`. Read `memory/ambiente-maquina.md` first.

## Looks

`looks.sh <name>` prints the ffmpeg filter chain for that treatment: analog wear, a horizontal tear, head switching, grain, a scan, and lighter variants of each. Preview at 540×960 before the final render.

When `face` is `yes`, fixed bands (tracking lines, tears) stay off the face height. Overall wear (grain, color bleed, scan) may cover the frame. A band that travels during a short transition may cross the face. When `face` is `no`, skip the face constraint.

## Transition sound

Synthesize it in ffmpeg. Pink and white noise in the mid band, a slow wow, a ramp in and a ramp out, only during the transition window. Nothing tonal. No vibrato and no echo. Those read as a ghost or a game. Keep each version in its own file with a one-line note of why it changed, so a later piece can go back.
