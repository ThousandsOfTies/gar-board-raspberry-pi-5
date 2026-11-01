# Board repository boundary

Own the board/OS identity, documented resource inventory, compiler/runtime names,
and startup/preparation selection. Keep Product names, camera modes, peripheral
models, application behavior, debounce choices and wiring uses in Products.
This is a documented subset, not a complete header or physical qualification.
Do not silently reinterpret gpiochip0 on kernels where it is not pinctrl-rp1.
SDKs, OS images, generated artifacts and machine connection data stay external.
