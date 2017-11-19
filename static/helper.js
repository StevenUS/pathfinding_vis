function midpoint(x1, y1, x2, y2) {
    return { 
        x: (x1 + x2)/2, 
        y: (y1 + y2)/2 
    }
}

function windowResized() {
    resizeCanvas(innerWidth, innerHeight)
}

function connectionExists(con) {
    let result = false
    edges.forEach(edge => {
        if (edge.id1 == con.id1 && edge.id2 == con.id2 ||
            edge.id2 == con.id1 && edge.id1 == con.id2
        ) {
            result = true
        }
    })
    return result
}

let heldNode = null
function mousePressed() {
    for (let id in nodes) {
        if (nodes[id].intersects(mouseX, mouseY)) {
            heldNode = nodes[id]
            break
        }
    }
}