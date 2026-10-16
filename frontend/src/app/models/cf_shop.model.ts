export interface login {
    username: string;
    password: string;
}

export interface loginResponse {
    access_token: string;
    token_type: string;
    username: string;
    role: string;
}


export interface staff {
    id: string;
    username: string;
    role: string;
}

export interface  staffCreate {
    username: string;
    password: string;
}

export interface staffCreateResponse {
    id: string;
    username: string;
    role: string;
}
export interface staffDeleteResponse {
    message: string;
}


export interface product {
    id: string;
    name: string;
    price: number;
    category: string;
    is_available: boolean;
    image: string;
}
export interface productCreate{
    name: string;
    price: number;
    image: string;
    category: string;
    is_available: boolean;
}

export interface productDetailResponse{
    name: string;
    price: number;
    image: string;
    category: string;
    is_available: boolean;
    id: string;
}

export interface productID{
    product_id: string;
}
export interface productUpdateID{
    product_id: string;
}
export interface productUpdateBody{
    name: string;
    price: number;
    image: string;
    category: string;
    is_available: boolean;
}
export interface productUpdateRespone{
    name: string;
    image: string;
    category: string;
    is_available: boolean;
    price: number;
    id: string;
}

export interface productDelete{
    product_id: string;
}
export interface productDeleteResponse{
    message: string;
}
