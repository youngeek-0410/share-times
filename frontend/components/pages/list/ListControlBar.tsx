import { FC } from "react";

import { HStack, InputGroup, InputLeftElement, InputRightElement, Input, Button, IconButton, Menu, MenuDivider, MenuButton, MenuList, MenuItem } from "@chakra-ui/react";
import { Search2Icon, SmallCloseIcon, ChevronDownIcon } from '@chakra-ui/icons'

const ListControlBar: FC = () => {
    return(
        <div>
            <HStack>
              <InputGroup width="2xl">
                <InputLeftElement
                    pointerEvents="none"
                    children={<Search2Icon color="gray.300" />}
                />
                <Input placeholder="検索する" />
                <InputRightElement 
                    pointerEvents="fill"
                    children={<IconButton aria-label="Clear Input" icon={<SmallCloseIcon />} />}/>
                </InputGroup>
                <Menu>
                    <MenuButton as={Button} rightIcon={<ChevronDownIcon marginLeft="6px"/>}>
                        並べ替える
                    </MenuButton>
                    <MenuList>
                        <MenuItem>名前順（前から）</MenuItem>
                        <MenuItem>名前順（後ろから）</MenuItem>
                        <MenuDivider />
                        <MenuItem>新しい更新順</MenuItem>
                        <MenuItem>古い更新順</MenuItem>
                    </MenuList>
                </Menu>
            </HStack>
        </div>
    )
}

export default ListControlBar