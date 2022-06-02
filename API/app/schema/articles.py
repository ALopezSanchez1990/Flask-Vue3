
articleInputPostSchema = {
    "type": "object",
    "properties": {
        "titulo": { 
            "type": "string" , 
            "maxLength": 256
            },
        "cuerpo": {
            "type": "string"
            },
        "categoria": { 
            "type": "number"
            },
        "etiqueta": { 
            "type": "string", 
            "maxLength": 32 
            },
    },
    "required": ["titulo", "cuerpo", "categoria", "etiqueta"]
}
