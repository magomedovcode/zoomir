export interface User {
    username: string;
    password: string;
}

export interface Brand {
    id: number;
    name: string;
    logo: string;
}

export interface Country {
    id: number;
    name: string;
    flag: string;
}

export interface ProductChapter {
    id: number;
    name: string;
}

export interface ProductCategory {
    id: number;
    name: string;
    product_chapter: ProductChapter;
}

export interface Attribute {
    id: number;
    name: string;
    value: string;
}

export interface AttributesPerCategory {
    id: number;
    name: string;
    attributes: Attribute[];
}

export interface Variant {
    id: number;
    name: string;
    price: string;
}

export interface Product {
    id: number;
    title: string;
    description: string;
    country: Country;
    product_category: ProductCategory;
    brand: Brand;
    variants: Variant[];
}

export interface ProductImage {
    id: number;
    image: string;
}

export interface VariantInProduct {
    id: number;
    name: string;
    price: string;
    product_images: ProductImage[];
    attributes: AttributesPerCategory[];
}

export interface ProductVariant {
    id: number;
    product_title: string;
    price: string;
    first_image: string;
    average_rating: number;
    reviews_count: number;
}

export interface ProductVariantResponse {
    count: number;
    next: string | null;
    previous: string | null;
    results: ProductVariant[];
}

export interface ReviewPhoto {
    id: number;
    photo: string;
}

export interface Review {
    id: number;
    user: string;
    title: string;
    comment: string;
    rating: number;
    date: string;
    review_photos: ReviewPhoto[];
}

export interface ProductDetail {
    id: number;
    title: string;
    description: string;
    brand: Brand;
    country: Country;
    product_category: ProductCategory;
    product_variants: VariantInProduct[];
    reviews: Review[];
    average_rating: number;
    reviews_count: number;
}

export interface FavoriteProduct {
    id: number;
    user: string;
    date: string;
    product: Product;
}

export interface FavoriteProductResponse {
    count: number;
    next: string | null;
    previous: string | null;
    results: FavoriteProduct[];
}

export interface ProductInCart {
    id: number;
    product_variant: ProductVariant;
    quantity: number;
}

export interface Cart {
    id: number;
    user: string;
    date: string;
    total_items: number;
    total_price: number;
    products_in_cart: ProductInCart[];
}

export interface ProductInOrder {
    id: number;
    price: string;
    quantity: number;
    product_variant: ProductVariant;
}

export enum Status {
    PENDING = 'pending',
    CONFIRMED = 'confirmed',
    SHIPPED = 'shipped',
    DELIVERED = 'delivered',
    CANCELED = 'cancelled'
}

export interface Order {
    id: number;
    user: string;
    address: string;
    phone: string;
    delivery_date: string;
    date: string;
    status: Status;
    total_price: number;
    products_in_order: ProductInOrder[];
}

export interface OrderResponse {
    count: number;
    next: string | null;
    previous: string | null;
    results: Order[];
}

export enum ProductOrdering {
    PRICE_DEFAULT = '',
    PRICE_ASC = 'price',
    PRICE_DESC = '-price'
}

export interface GetProductsParams {
    brand?: number[];
    country?: number[];
    ordering?: ProductOrdering;
    page?: number;
    page_size?: number;
    price_max?: number;
    price_min?: number;
    product_category?: number[];
    search?: string;
}

export interface CreateReviewBody {
    productId: number;
    title: string;
    rating: number;
    comment: string;
    photos: File[];
}

export interface OrderProduct  {
    product_variant: number,
    quantity: number
}

export interface CreateOrderBody {
    address: string,
    phone: string,
    delivery_date: string,
    products: OrderProduct[]
}
