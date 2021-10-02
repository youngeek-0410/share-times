import { FC } from 'react'

import { useNumberInput } from '@chakra-ui/number-input'
import { HStack, Button, Input, Text } from '@chakra-ui/react'

const NumberInputForm: FC = () => {
    const {
        getInputProps,
        getIncrementButtonProps,
        getDecrementButtonProps,
    } = useNumberInput({
        step: 1,
        defaultValue: 5,
        min: 0,
        max: 180,
        precision: 0,
    })

    const increment = getIncrementButtonProps()
    const decrement = getDecrementButtonProps()
    const input = getInputProps()

    return (
        <HStack maxW="320px">
            <Button {...increment}>+</Button>
            <Input {...input} width="60px" />
            <Text>分</Text>
            <Button {...decrement}>-</Button>
        </HStack>
    )
}

export default NumberInputForm