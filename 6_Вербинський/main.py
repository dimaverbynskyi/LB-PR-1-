import os
import time
import matplotlib.pyplot as plt
from generators import generate_polygon, visualize_polygon
from algorithms import gauss_area, monte_carlo_area

def main():
    img_dir = os.path.join(os.path.dirname(__file__), '..', 'images')
    os.makedirs(img_dir, exist_ok=True)
    
    print("=== 1. Генерація полігонів ===")
    polygons = {}
    vertices_counts = [10, 50, 100, 1000]
    
    for n in vertices_counts:
        poly = generate_polygon(num_points=n)
        polygons[n] = poly
        if n in [10, 50, 100]:
            visualize_polygon(poly, filename=os.path.join(img_dir, f"polygon_{n}.png"))
            
    print("\n=== 2. Дослідження точності Монте-Карло ===")
    poly_50 = polygons[50]
    true_area = poly_50.area 
    m_values = [100, 1000, 10000, 100000]
    errors = []
    
    for m in m_values:
        mc_area = monte_carlo_area(poly_50, m)
        error = abs(mc_area - true_area) / true_area * 100
        errors.append(error)
        print(f"Ітерацій M={m}: Площа = {mc_area:.2f}, Похибка = {error:.2f}%")
        
    plt.figure(figsize=(8, 5))
    plt.plot(m_values, errors, marker='o', linestyle='-', color='b')
    plt.xscale('log')
    plt.xlabel('Кількість ітерацій (M)')
    plt.ylabel('Відносна похибка (%)')
    plt.title('Збіжність методу Монте-Карло')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig(os.path.join(img_dir, "error_plot.png"))
    plt.close()
    
    print("\n=== 3. Аналіз продуктивності (Бенчмарк) ===")
    print(f"{'Вершин (N)':<12} | {'Shapely (мс)':<15} | {'Гаус (мс)':<15} | {'Монте-Карло (мс)':<15}")
    print("-" * 65)
    
    M_ITERATIONS = 100000
    for n in vertices_counts:
        poly = polygons[n]
        start_time = time.perf_counter()
        _ = poly.area
        shapely_time = (time.perf_counter() - start_time) * 1000
        
        start_time = time.perf_counter()
        _ = gauss_area(poly)
        gauss_time = (time.perf_counter() - start_time) * 1000
        
        start_time = time.perf_counter()
        _ = monte_carlo_area(poly, M_ITERATIONS)
        mc_time = (time.perf_counter() - start_time) * 1000
        
        print(f"{n:<12} | {shapely_time:<15.4f} | {gauss_time:<15.4f} | {mc_time:<15.4f}")

if __name__ == "__main__":
    main()