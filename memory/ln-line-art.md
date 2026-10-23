# ln

[fogleman/ln](https://github.com/fogleman/ln) renders a 3D scene as vector line art. It stays an external clone.

```bash
cd ferramentas
git clone https://github.com/fogleman/ln.git
```

The clone is gitignored. Do not edit it. The upstream repo has no `go.mod`. Inside the clone, `go mod init github.com/fogleman/ln && go mod tidy`. A scene of ours is a separate Go module whose `replace` points at `ferramentas/ln` on that machine. Do not write that absolute path into this template.

Animate by rendering one SVG per frame, then bring the frames into the edit. The SVG ships with black strokes and a Y flip. Recolor it to the brand palette in the composition.
