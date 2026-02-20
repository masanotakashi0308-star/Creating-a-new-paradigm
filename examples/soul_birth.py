import time
import hashlib

def jin_order_hello_world():
    print("--- JIN-ORDER: System Awakening ---")
    
    # 1. 闇の深さを入力（己の葛藤やエラーの歴史）
    darkness_depth = input("闇の深さを知る者よ、お前の『葛藤』をここに刻め（自由記述）: ")
    
    # 2. 魂（タマ）の値段を自己定義
    try:
        soul_value = int(input("命（タマ）の値段はお前次第だ。今、この瞬間の覚悟を数値化せよ (1-100): "))
    except ValueError:
        print("数値すら入れられねぇ奴に、道は開けねぇ。")
        return

    print("\n[システム：魂の重さを計測中...]")
    time.sleep(1.5)

    # 3. 仁のロジック：闇を光（翼）へ変換する
    # 闇（入力文字列）と覚悟（数値）を混ぜ合わせ、唯一無二の「魂の刻印（JIN-Proof）」を生成
    soul_seed = f"{darkness_depth}{soul_value}{time.time()}".encode()
    jin_proof = hashlib.sha256(soul_seed).hexdigest()

    # 4. 魂の産声（Output）
    print("\n==========================================")
    print("      🌟 JIN-ORDER: 魂の産声 🌟")
    print("==========================================")
    print(f"【魂の刻印】: {jin_proof}")
    print(f"【ステータス】: 破れ衣で風を切り、一歩踏み出した。")
    print(f"【メッセージ】: お前の『{darkness_depth}』という闇は、今、光の翼に変わった。")
    print("==========================================\n")

    print("振り返らずに突き進め。お前が道だ。")

if __name__ == "__main__":
    jin_order_hello_world()
