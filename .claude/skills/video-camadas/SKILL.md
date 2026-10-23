---
name: video-camadas
description: Build a person mask, a green-screen matte, a face-free zone, a zoom table, and a layered preview for a talking-head video. Use when face is yes and the edit needs text behind the person or a measured face zone.
---

# video-camadas

One command, `ferramentas/video-camadas/video-camadas`. Local. No API. Read the last stdout line.

| Task | Command |
|---|---|
| Person mask from the zoomed base | `video-camadas pessoa base_zoom.mp4 mask.mkv --w 960` |
| Green screen | `video-camadas verde recording.mp4 mask.mkv --sim 0.15 --blend 0.08` |
| Head and chin zone | `video-camadas faces base.mp4 faces.json --cada 1` |
| Zoom table | `video-camadas zoom chop.mp4 base_zoom.mp4 --w 960 --tabela "0:1.06:4.4"` |
| Layered preview | `video-camadas camadas base_zoom.mp4 "preview N.mp4" --atras behind.mov --mascara mask.mkv --frente front.mov --legenda captions.mkv` |

The mask comes from the zoomed base, or it will not follow the zoom. Skip this skill when `face` in `memory/config.md` is `no`. `sfx` is a legacy synthetic bed. Prefer recorded samples when the creator has a sound pattern on file.
