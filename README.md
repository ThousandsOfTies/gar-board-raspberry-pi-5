# gar-board-raspberry-pi-5

Raspberry Pi 5をProductへ組み込むための独立した基板リポジトリです。
`board.json`がプロファイルを示し、`profiles/raspberry-pi-os-arm64.json`が
OS/ABI、GPIO・SPI・I2C資源、Python実行先、起動方式を持ちます。
Productがアプリ・gar-toolsとともにsubmoduleで固定します。

このプロファイルは、既存構成と同じく`/dev/gpiochip0`が`pinctrl-rp1`であるOSを対象にします。
番号の割当が異なるOSに、このプロファイルをそのまま適用しません。
GPIO番号はRP1のライン番号、`line_pins`は40ピンヘッダーの物理番号です。
記載範囲は利用する端子の一部に限ります。

アプリの意味、接続するカメラや液晶、端子の用途、デバウンス、通信先はProductが持ちます。
カメラのフレームレートや`/dev/video0`の列挙順を基板の保証には含めません。
SPIの50MHzは既存GAR契約を引き継ぐプロファイル上限です。

`startup.manager=gar-target`は既存GARの導入・サービス管理を選択します。
Productの配布物にroot管理のsystemdファイルやインストーラーを複製しません。
従来のTarget Packは互換経路としてgar-toolsに残り、GAR本体の探索・transportは変更しません。
このrepoは新しいProduct構成で選択する基板情報の正本です。

出典: [Raspberry Pi公式ハードウェア資料](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)、
[公式GPIOホワイトペーパー](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)。
今回の分離後の実機への導入試験は実施していません。
