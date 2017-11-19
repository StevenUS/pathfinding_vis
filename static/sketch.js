// frames = JSON.parse(frames)

let nodes = {},
    edges = []

const input = [
    {
        id: 0,
        w: 10,
        edges: [ {id:1, w:10}, {id:2, w:5} ]
    },
    {
        id: 1,
        w: 2,
        edges: [ {id:2, w:4} ]
    },
    {
        id: 2,
        w: 50,
        edges: [ {id:0, w:3} ]
    }
]

function setup() {
    createCanvas(innerWidth, innerHeight)
    input.forEach(node => {
        nodes[node.id] = new Node(node)
        node.edges.forEach(edge => {
            let con = { 
                id1: node.id,
                id2: edge.id,
                w: edge.w,
                hl: true
            }
            if (!connectionExists(con)) {
                edges.push(con)
            }
        })
    })
}

function draw() {
    background(50)
    strokeWeight(1)
    textAlign(CENTER, CENTER)

    edges.forEach(edge => {
        strokeWeight(2)
        let node1 = nodes[edge.id1],
            node2 = nodes[edge.id2],
            w = edge.w
        fill(255)
        if (edge.hl) {
            stroke(255, 50, 50)
        } else {
            stroke(200)
        }
        let x1 = node1.pos.x,
            y1 = node1.pos.y,
            x2 = node2.pos.x,
            y2 = node2.pos.y
        line(x1, y1, x2, y2)
        stroke(0)
        let mid = midpoint(x1, y1, x2, y2)
        strokeWeight(3)
        text(w, mid.x, mid.y)
    })

    for (let id in nodes) {
        nodes[id].show()
    }

    if (heldNode) {
        heldNode.pos.x = mouseX
        heldNode.pos.y = mouseY
    }

    if (!mouseIsPressed) {
        heldNode = null
    }
}