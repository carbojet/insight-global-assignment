import math

def paginate(items, page: int, pageSize: int):
    totalItems = len(items)
    totalPages = math.ceil(totalItems / pageSize)

    start = (page - 1) * pageSize
    end = start + pageSize

    return {
        "data": items[start:end],
        "meta": {
            "page": page,
            "pageSize": pageSize,
            "totalItems": totalItems,
            "totalPages": totalPages,
            "hasNext": page < totalPages
        }
    }
